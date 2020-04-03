# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "wmo"
app_title = "World Memon Organization"
app_publisher = "Ashfaq Khatri"
app_description = "Prototype for WMO"
app_icon = "octicon octicon-globe"
app_color = "grey"
app_email = "kiet_mak@yahoo.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/wmo/css/wmo.css"
# app_include_js = "/assets/wmo/js/wmo.js"

# include js, css files in header of web template
# web_include_css = "/assets/wmo/css/wmo.css"
# web_include_js = "/assets/wmo/js/wmo.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "wmo.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "wmo.install.before_install"
# after_install = "wmo.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "wmo.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"wmo.tasks.all"
# 	],
# 	"daily": [
# 		"wmo.tasks.daily"
# 	],
# 	"hourly": [
# 		"wmo.tasks.hourly"
# 	],
# 	"weekly": [
# 		"wmo.tasks.weekly"
# 	]
# 	"monthly": [
# 		"wmo.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "wmo.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "wmo.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "wmo.task.get_dashboard_data"
# }
fixtures=['Custom Field']

