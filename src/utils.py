
def sec_to_mmss(seconds):
    m, s = divmod(seconds, 60)
    if seconds >= 3600:
        h, m = divmod(m, 60)
        m, s = h, m # Move the values one delimiter to the right
        return '{:2d}{:02d}'.format(m, s) # Returns ?H:SS String
    else:
        return '{:02d}{:02d}'.format(m, s) # Returns MMSS String