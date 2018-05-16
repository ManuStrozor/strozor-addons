import xbmcaddon
import xbmcgui

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')

line1 = "Première ligne,"
line2 = "deuxième ligne, et..."
line3 = "troisième ligne !"

xbmcgui.Dialog().ok(addonname, line1, line2, line3)
