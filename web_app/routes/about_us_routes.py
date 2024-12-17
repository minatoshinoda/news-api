from flask import Blueprint, request, render_template

about_us_routes = Blueprint("about_us_routes", __name__)

@about_us_routes.route("/about/us") #routes to the about us html file
def about_list():
    about = [ #each developer's introduction
        {
            'name': 'Abhi Meka',
            'info': 'Class of 2026, Finance & OPAN',
            'url': 'https://media.licdn.com/dms/image/v2/D4E03AQGerYqQ0kvzzA/profile-displayphoto-shrink_400_400/B4EZPQkao7HkAs-/0/1734371027893?e=1740009600&v=beta&t=xzMM4yk8cWSed0-jjFUEWzuP2tTtDAA3QAfJ6NLwdb4'
        },
        {
            'name': 'Minato Shinoda',
            'info': 'Class of 2026, Marketing & OPAN',
            'url': 'https://media.licdn.com/dms/image/v2/D4E03AQF3ruzP_x4gXg/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1727844606886?e=2147483647&v=beta&t=CpTcuwHH8T9mqZ_5D1L6dWTYLh-FZ1N0RDATn67cHjU'
        },
        {
            'name': 'Sneha Selvaraj',
            'info': 'Class of 2026, Marketing & OPAN',
            'url': 'https://media.licdn.com/dms/image/v2/D5603AQGDnbqaGnITQA/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1672116330417?e=2147483647&v=beta&t=u_VF3X2ip4FdFHDc6tUjK-bro5zHOSv2cbOJfyDFNGQ'
        }
    ]

    return render_template("about_us.html", about=about)