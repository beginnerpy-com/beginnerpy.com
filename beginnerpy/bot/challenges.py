from flask import Blueprint, render_template
from beginnerpy.models import *
from beginnerpy.func import getSideNav

static_folder = "../static/bot"
template_folder = "../templates/bot"
challenges_blueprint = Blueprint(
	"challenges",
	__name__,
	static_folder=str(static_folder),
	static_url_path="/static/bot",
	template_folder=str(template_folder),
	url_prefix="/admin/bot",
)


@challenges_blueprint.route("/challenges")
def challenge_home():
	context = {
		"sidenav": getSideNav(),
		"endpoint": "challenges",
		"property": "admin",
	}
	return render_template("challenge_list.html", **context)


@challenges_blueprint.route("/challenges/<challenge_slug>")
def view_challenge(challenge_slug):
	return render_template("challenge_list.html")
