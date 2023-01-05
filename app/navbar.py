import dash_bootstrap_components as dbc


def navbar():
    return dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink('Trail Activity Lexicon',
                                    id='trail-lexicon',
                                    href='assets/traillexicon.html',
                                    external_link=True,
                                    style={'margin-top': '8px'}
                                    )),
            # dbc.NavItem(dbc.NavLink('3D Built Environment',
            #                         id='building-map-link',
            #                         href='/3d-built-environment',
            #                         )),
            # dbc.NavItem(dbc.NavLink('Critical Assets',
            #                         id='critical-assets',
            #                         href='/critical-assets',
            #                         )),
            # dbc.NavItem(dbc.NavLink('Flood Risk and SLR',
            #                         id='terrain-map-link',
            #                         href='/flood-risk-and-slr',
            #                         )),
            # dbc.NavItem(dbc.NavLink('LiDAR Point Cloud',
            #                         id='lidar-point-cloud-link',
            #                         href='/lidar-point-cloud',
            #                         ))
        ],
        brand='Data Analysis of Trail Experiences and Usage',
        brand_href='/',
        brand_style={'font-size': '2em'},
        color="#",
        fluid=True,
        dark=False,
        class_name='px-4 navbar-light',
        style={'box-shadow': '1px 1px 1px lightgrey'}
    )
