import numpy as np
from datetime import datetime
try:
  import netCDF4 as netCDF
except:
  import netCDF3 as netCDF


def nc_create_roms_bdry_file(filename, grd, ocean_time):

    # create file
    nc = netCDF.Dataset(filename, 'w', format='NETCDF3_64BIT')
    nc.Description = 'ROMS file'
    nc.Author = 'pyroms_toolbox.nc_create_roms_file'
    nc.Created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nc.title = 'ROMS file'

    nc.createDimension('xi_rho', np.size(grd.hgrid.mask_rho,1))
    nc.createDimension('xi_u', np.size(grd.hgrid.mask_u,1))
    nc.createDimension('xi_v', np.size(grd.hgrid.mask_v,1))
    nc.createDimension('xi_psi', np.size(grd.hgrid.mask_psi,1))
    nc.createDimension('eta_rho', np.size(grd.hgrid.mask_rho,0))
    nc.createDimension('eta_u', np.size(grd.hgrid.mask_u,0))
    nc.createDimension('eta_v', np.size(grd.hgrid.mask_v,0))
    nc.createDimension('eta_psi', np.size(grd.hgrid.mask_psi,0))
    nc.createDimension('s_rho', grd.vgrid.N)
    nc.createDimension('s_w', grd.vgrid.Np)
    nc.createDimension('ocean_time', None)
    # nc.createDimension('zeta_time', 1)
    # nc.createDimension('salt_time', 1)
    # nc.createDimension('temp_time', 1)
    # nc.createDimension('v2d_time', 1)
    # nc.createDimension('v3d_time', 1)

    # write time and grid information
    nc.createVariable('theta_s', 'f8', ())
    nc.variables['theta_s'].long_name = 'S-coordinate surface control parameter'
    nc.variables['theta_s'][:] = grd.vgrid.theta_s

    nc.createVariable('theta_b', 'f8', ())
    nc.variables['theta_b'].long_name = 'S-coordinate bottom control parameter'
    nc.variables['theta_b'][:] = grd.vgrid.theta_b

    nc.createVariable('Tcline', 'f8', ())
    nc.variables['Tcline'].long_name = 'S-cordinate surface/bottom layer width'
    nc.variables['Tcline'].units = 'meter'
    nc.variables['Tcline'][:] = grd.vgrid.Tcline

    nc.createVariable('hc', 'f8', ())
    nc.variables['hc'].long_name = 'S-coordinate parameter, critical depth'
    nc.variables['hc'].units = 'meter'
    nc.variables['hc'][:] = grd.vgrid.hc

    nc.createVariable('s_rho', 'f8', ('s_rho'))
    nc.variables['s_rho'].long_name = 'S-coordinate at RHO-points'
    nc.variables['s_rho'].valid_min = '-1.0'
    nc.variables['s_rho'].valid_max = '0.0'
    nc.variables['s_rho'].field = 's_rho,scalar'
    nc.variables['s_rho'][:] = grd.vgrid.s_rho

    nc.createVariable('s_w', 'f8', ('s_w'))
    nc.variables['s_w'].long_name = 'S-coordinate at W-points'
    nc.variables['s_w'].valid_min = '-1.0'
    nc.variables['s_w'].valid_max = '0.0'
    nc.variables['s_w'].field = 's_w,scalar'
    nc.variables['s_w'][:] = grd.vgrid.s_w

    nc.createVariable('Cs_r', 'f8', ('s_rho'))
    nc.variables['Cs_r'].long_name = 'S-coordinate stretching curves at RHO-points'
    nc.variables['Cs_r'].valid_min = '-1.0'
    nc.variables['Cs_r'].valid_max = '0.0'
    nc.variables['Cs_r'].field = 'Cs_r,scalar'
    nc.variables['Cs_r'][:] = grd.vgrid.Cs_r

    nc.createVariable('Cs_w', 'f8', ('s_w'))
    nc.variables['Cs_w'].long_name = 'S-coordinate stretching curves at W-points'
    nc.variables['Cs_w'].valid_min = '-1.0'
    nc.variables['Cs_w'].valid_max = '0.0'
    nc.variables['Cs_w'].field = 'Cs_w,scalar'
    nc.variables['Cs_w'][:] = grd.vgrid.Cs_w

    nc.createVariable('h', 'f8', ('eta_rho', 'xi_rho'))
    nc.variables['h'].long_name = 'bathymetry at RHO-points'
    nc.variables['h'].units ='meter'
    nc.variables['h'].coordinates = 'lon_rho lat_rho'
    nc.variables['h'].field = 'bath, scalar'
    nc.variables['h'][:] = grd.vgrid.h


    nc.createVariable('ocean_time', 'f8', ('ocean_time'))
    nc.variables['ocean_time'].long_name = ocean_time.long_name
    nc.variables['ocean_time'].units = ocean_time.units
    try:
        nc.variables['ocean_time'].field = ocean_time.field
    except:
        nc.variables['ocean_time'].field = ' '

    # debug: modified by Hongjing Chen in 2024/04/06
    # added the zeta_time, salt_time, temp_time, v2d_time and v3d_time coordinates in bdry nc file.
    # debug start ======================================
    # nc.createVariable('zeta_time', 'f8', ('zeta_time'))
    # nc.variables['zeta_time'].long_name = ocean_time.long_name
    # nc.variables['zeta_time'].units = ocean_time.units
    # try:
    #     nc.variables['zeta_time'].field = ocean_time.field
    # except:
    #     nc.variables['zeta_time'].field = ' '
        
    # nc.createVariable('salt_time', 'f8', ('salt_time'))
    # nc.variables['salt_time'].long_name = ocean_time.long_name
    # nc.variables['salt_time'].units = ocean_time.units
    # try:
    #     nc.variables['salt_time'].field = ocean_time.field
    # except:
    #     nc.variables['salt_time'].field = ' '

    # nc.createVariable('temp_time', 'f8', ('temp_time'))
    # nc.variables['temp_time'].long_name = ocean_time.long_name
    # nc.variables['temp_time'].units = ocean_time.units
    # try:
    #     nc.variables['temp_time'].field = ocean_time.field
    # except:
    #     nc.variables['temp_time'].field = ' '

    # nc.createVariable('v2d_time', 'f8', ('v2d_time'))
    # nc.variables['v2d_time'].long_name = ocean_time.long_name
    # nc.variables['v2d_time'].units = ocean_time.units
    # try:
    #     nc.variables['v2d_time'].field = ocean_time.field
    # except:
    #     nc.variables['v2d_time'].field = ' '

    # nc.createVariable('v3d_time', 'f8', ('v3d_time'))
    # nc.variables['v3d_time'].long_name = ocean_time.long_name
    # nc.variables['v3d_time'].units = ocean_time.units
    # try:
    #     nc.variables['v3d_time'].field = ocean_time.field
    # except:
    #     nc.variables['v3d_time'].field = ' '
    
    # debug end =========================================

    nc.close()
