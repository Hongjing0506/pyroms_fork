r'''
Author: ChenHJ
Date: 2024-06-28 17:30:24
LastEditors: ChenHJ
LastEditTime: 2024-06-28 20:13:44
FilePath: /mylib/pyroms/pyroms_toolbox/pyroms_toolbox/Grid_CMEMS/get_nc_Grid_CMEMS.py
Description: 
'''
import numpy as np
import pyroms
import netCDF4
from mpl_toolkits.basemap import pyproj
from pyroms_toolbox.Grid_CMEMS import Grid_CMEMS


def get_nc_Grid_CMEMS(grdfile, name='CMEMS', xrange=(60,175), yrange=(120, 190)):

    """
    grd = get_nc_Grid_CMEMS(grdfile)

    Load grid object for CMEMS
    """

    nc = netCDF4.Dataset(grdfile)
    lon = nc.variables['longitude'][:]
    lat = nc.variables['latitude'][:]
    depth = nc.variables['depth'][:]
    # ssh = nc.variables['zos'][0,:,:]
    var = nc.variables['thetao'][0,:,:,:]
    nc.close()

    lon_t, lat_t = np.meshgrid(lon, lat)

    lonv = 0.5 * (lon[1:] + lon[:-1])
    lonv = np.insert(lonv, 0, 2*lon[0] - lonv[0])
    lonv = np.append(lonv, 360.1)

    latv = 0.5 * (lat[1:] + lat[:-1])
    latv = np.insert(latv, 0, [2*lat[0] - latv[0]])
    latv = np.append(latv, [2*lat[-1] - latv[-1]])

    lon_vert, lat_vert = np.meshgrid(lonv, latv)

    mask_t = np.array(~var[:].mask, dtype='int')

    z_t = np.tile(depth,(mask_t.shape[2],mask_t.shape[1],1)).T

    depth_bnds = np.zeros(len(depth)+1)
    for i in range(1,len(depth)):
        depth_bnds[i] = 0.5 * (depth[i-1] + depth[i])
    depth_bnds[-1] = 6000  # maybe wrong here; don't know the real value

    bottom = pyroms.utility.get_bottom(var[::-1,:,:], mask_t[0], spval=var.fill_value)
    nlev = len(depth)
    bottom = (nlev-1) - bottom
    h = np.zeros(mask_t[0,:].shape)
    for i in range(mask_t[0,:].shape[1]):
        for j in range(mask_t[0,:].shape[0]):
            if mask_t[0,j,i] == 1:
                h[j,i] = depth_bnds[int(bottom[j,i])+1]

    angle = np.zeros((lat.shape[0], lon.shape[0]))

#   geod = pyproj.Geod(ellps='WGS84')
#   az_forward, az_back, dx = geod.inv(lon_vert[:,:-1], lat_vert[:,:-1], lon_vert[:,1:], lat_vert[:,1:])
#   angle = 0.5 * (az_forward[1:,:] + az_forward[:-1,:])
#   angle = (90 - angle) * np.pi/180.

    return Grid_CMEMS(lon_t, lat_t, lon_vert, lat_vert, mask_t, z_t, h, angle, name, xrange, yrange)
