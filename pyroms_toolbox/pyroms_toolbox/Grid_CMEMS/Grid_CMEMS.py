class Grid_CMEMS(object):
    """
    Grid object for CEMES
    """

    def __init__(self, lon_t, lat_t, lon_vert, lat_vert, mask_t, z_t, h, angle, name, xrange, yrange):

        self.name = name
        
        #debug by hongjing ======
        self.xrange = xrange
        self.yrange = yrange 
        self.lon_t = lon_t[yrange[0]:yrange[1]+1, xrange[0]:xrange[1]+1]
        self.lat_t = lat_t[yrange[0]:yrange[1]+1, xrange[0]:xrange[1]+1]

        self.lon_vert = lon_vert[yrange[0]-1:yrange[1]+1, xrange[0]-1:xrange[1]+1]
        self.lat_vert = lat_vert[yrange[0]-1:yrange[1]+1, xrange[0]-1:xrange[1]+1]

        self.mask_t = mask_t[:,yrange[0]:yrange[1]+1, xrange[0]:xrange[1]+1]

        self.z_t = z_t

        self.h = h[yrange[0]:yrange[1]+1, xrange[0]:xrange[1]+1]

        self.angle = angle[yrange[0]:yrange[1]+1, xrange[0]:xrange[1]+1]
