from weecfg.extension import ExtensionInstaller

# Copyright 2023 David Baetge
# Distributed under the terms of the GNU Public License (GPLv3)


def loader():
    return BasicInstaller()


class BasicInstaller(ExtensionInstaller):
    def __init__(self):
        super(BasicInstaller, self).__init__(
            version="3.5.0-alpha1",
            name="weewx-wdc",
            description="Weather Data Center skin for WeeWX.",
            author="David Baetge",
            author_email="david.baetge@gmail.com",
            config={
                "StdReport": {
                    "WdcReport": {
                        "skin": "weewx-wdc",
                        "enable": "true",
                    }
                }
            },
            files=[
                (
                    "bin/user",
                    [
                        "bin/user/weewx_wdc.py",
                    ],
                ),
                (
                    "skins/weewx-wdc",
                    [
                        "skins/weewx-wdc/index.html.tmpl",
                        "skins/weewx-wdc/yesterday.html.tmpl",
                        "skins/weewx-wdc/week.html.tmpl",
                        "skins/weewx-wdc/month.html.tmpl",
                        "skins/weewx-wdc/dwd.html.tmpl",
                        "skins/weewx-wdc/sensor-status.html.tmpl",
                        "skins/weewx-wdc/computer-monitor.html.tmpl",
                        "skins/weewx-wdc/day-archive/day-%Y-%m-%d.html.tmpl",
                        "skins/weewx-wdc/month-%Y-%m.html.tmpl",
                        "skins/weewx-wdc/NOAA/NOAA-%Y-%m.txt.tmpl",
                        "skins/weewx-wdc/year.html.tmpl",
                        "skins/weewx-wdc/NOAA/NOAA-%Y.txt.tmpl",
                        "skins/weewx-wdc/year-%Y.html.tmpl",
                        "skins/weewx-wdc/statistics.html.tmpl",
                        "skins/weewx-wdc/celestial.html.tmpl",
                        "skins/weewx-wdc/about.html.tmpl",
                        "skins/weewx-wdc/externals.html.tmpl",
                        "skins/weewx-wdc/offline.html.tmpl",
                        "skins/weewx-wdc/manifest.json.tmpl",
                        "skins/weewx-wdc/icon-192x192.png",
                        "skins/weewx-wdc/icon-256x256.png",
                        "skins/weewx-wdc/icon-384x384.png",
                        "skins/weewx-wdc/icon-512x512.png",
                        "skins/weewx-wdc/skin.conf",
                        "skins/weewx-wdc/lang/de.conf",
                        "skins/weewx-wdc/lang/en.conf",
                        "skins/weewx-wdc/lang/it.conf",
                        "skins/weewx-wdc/lang/nl.conf",
                        "skins/weewx-wdc/lang/fi.conf",
                        "skins/weewx-wdc/service-worker.js",
                        "skins/weewx-wdc/dist/main.css",
                        "skins/weewx-wdc/dist/main.js",
                        "skins/weewx-wdc/dist/live-updates.js",
                        "skins/weewx-wdc/dist/assets/IBMPlexMono-Regular.woff2",
                        "skins/weewx-wdc/dist/assets/IBMPlexMono-Regular.woff",
                        "skins/weewx-wdc/dist/assets/IBMPlexSans-Regular.woff2",
                        "skins/weewx-wdc/dist/assets/IBMPlexSans-Regular.woff",
                        "skins/weewx-wdc/dist/assets/IBMPlexSans-SemiBold.woff2",
                        "skins/weewx-wdc/dist/assets/IBMPlexSans-SemiBold.woff",
                        "skins/weewx-wdc/dist/assets/IBMPlexSerif-Regular.woff2",
                        "skins/weewx-wdc/dist/assets/IBMPlexSerif-Regular.woff",
                        "skins/weewx-wdc/favicon.ico",
                        "skins/weewx-wdc/plotly-custom-build.min.js",
                        "skins/weewx-wdc/includes/html-head.inc",
                        "skins/weewx-wdc/includes/section-heading.inc",
                        "skins/weewx-wdc/includes/almanac-tile.inc",
                        "skins/weewx-wdc/includes/almanac-tile-simple.inc",
                        "skins/weewx-wdc/includes/almanac-moon-detail-tile.inc",
                        "skins/weewx-wdc/includes/almanac-sun-detail-tile.inc",
                        "skins/weewx-wdc/includes/combined-diagram-tile.inc",
                        "skins/weewx-wdc/includes/data-table-tile.inc",
                        "skins/weewx-wdc/includes/diagram-tile.inc",
                        "skins/weewx-wdc/includes/gauge-tile.inc",
                        "skins/weewx-wdc/includes/diagram-tile-wind-rose.inc",
                        "skins/weewx-wdc/includes/dwd-warning.inc",
                        "skins/weewx-wdc/includes/stat-tile.inc",
                        "skins/weewx-wdc/includes/stat-tile-xaggs.inc",
                        "skins/weewx-wdc/includes/stat-tile-modals.inc",
                        "skins/weewx-wdc/includes/conditions-table.inc",
                        "skins/weewx-wdc/includes/climatological-days.inc",
                        "skins/weewx-wdc/includes/ui-shell.inc",
                        "skins/weewx-wdc/includes/footer.inc",
                        "skins/weewx-wdc/includes/body-classic.inc",
                        "skins/weewx-wdc/includes/body-alternative.inc",
                        "skins/weewx-wdc/includes/forecast.inc",
                        "skins/weewx-wdc/includes/forecast-table.inc",
                        "skins/weewx-wdc/includes/year-stats-table.inc",
                        "skins/weewx-wdc/includes/icons/barometer.svg",
                        "skins/weewx-wdc/includes/pictograms/sun.svg",
                        "skins/weewx-wdc/includes/pictograms/moon.svg",
                        "skins/weewx-wdc/includes/icons/battery.svg",
                        "skins/weewx-wdc/includes/icons/signal.svg",
                        "skins/weewx-wdc/includes/icons/soil-moist.svg",
                        "skins/weewx-wdc/includes/icons/soil-temp.svg",
                        "skins/weewx-wdc/includes/icons/lightning.svg",
                        "skins/weewx-wdc/includes/icons/noise.svg",
                        "skins/weewx-wdc/includes/icons/voltage.svg",
                        "skins/weewx-wdc/includes/icons/forecast.svg",
                        "skins/weewx-wdc/includes/icons/leaf.svg",
                        "skins/weewx-wdc/includes/icons/hail.svg",
                        "skins/weewx-wdc/includes/icons/snow.svg",
                        "skins/weewx-wdc/includes/icons/snow-depth.svg",
                        "skins/weewx-wdc/includes/icons/snow-moist.svg",
                        "skins/weewx-wdc/includes/icons/cloud-base.svg",
                        "skins/weewx-wdc/includes/icons/dew-point.svg",
                        "skins/weewx-wdc/includes/icons/et.svg",
                        "skins/weewx-wdc/includes/icons/app-temp.svg",
                        "skins/weewx-wdc/includes/icons/heat-index.svg",
                        "skins/weewx-wdc/includes/icons/humidity.svg",
                        "skins/weewx-wdc/includes/icons/rain-rate.svg",
                        "skins/weewx-wdc/includes/icons/rain.svg",
                        "skins/weewx-wdc/includes/icons/radiation.svg",
                        "skins/weewx-wdc/includes/icons/temp.svg",
                        "skins/weewx-wdc/includes/icons/uv.svg",
                        "skins/weewx-wdc/includes/icons/wind-chill.svg",
                        "skins/weewx-wdc/includes/icons/wind-run.svg",
                        "skins/weewx-wdc/includes/icons/wind-direction.svg",
                        "skins/weewx-wdc/includes/icons/wind-direction.inc",
                        "skins/weewx-wdc/includes/icons/wind-gust.svg",
                        "skins/weewx-wdc/includes/icons/wind-speed.svg",
                        "skins/weewx-wdc/includes/icons/sunrise.svg",
                        "skins/weewx-wdc/includes/icons/sunset.svg",
                        "skins/weewx-wdc/includes/icons/moon.svg",
                        "skins/weewx-wdc/includes/icons/moonrise.svg",
                        "skins/weewx-wdc/includes/icons/moonset.svg",
                        "skins/weewx-wdc/includes/icons/github.svg",
                        "skins/weewx-wdc/includes/icons/mask.svg",
                        "skins/weewx-wdc/includes/icons/wdc.svg",
                        "skins/weewx-wdc/includes/icons/forecast/B1.svg",
                        "skins/weewx-wdc/includes/icons/forecast/B2.svg",
                        "skins/weewx-wdc/includes/icons/forecast/BK.svg",
                        "skins/weewx-wdc/includes/icons/forecast/CL.svg",
                        "skins/weewx-wdc/includes/icons/forecast/FW.svg",
                        "skins/weewx-wdc/includes/icons/forecast/OV.svg",
                        "skins/weewx-wdc/includes/icons/forecast/SC.svg",
                        "skins/weewx-wdc/includes/icons/forecast/rain.svg",
                        "skins/weewx-wdc/includes/icons/forecast/snow.svg",
                        "skins/weewx-wdc/includes/icons/forecast/sleet.svg",
                        "skins/weewx-wdc/includes/icons/forecast/fog.svg",
                        "skins/weewx-wdc/includes/icons/forecast/haze.svg",
                        "skins/weewx-wdc/includes/icons/forecast/snow--scattered.svg",
                        "skins/weewx-wdc/includes/icons/forecast/rain--scattered.svg",
                        "skins/weewx-wdc/includes/icons/forecast/thunderstorm.svg",
                        "skins/weewx-wdc/includes/icons/forecast/thunderstorm--scattered.svg",
                        "skins/weewx-wdc/includes/icons/forecast/rain-drop.svg",
                        "skins/weewx-wdc/includes/icons/forecast/snowflake.svg",
                    ],
                ),
            ],
        )
