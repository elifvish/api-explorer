import frappe
from api_explorer.api_explorer.generate_api_docs import get_app_title_and_version

def get_context(context):
    context.apps = frappe.get_installed_apps()
    context.app_titles = {}
    context.default_app = context.apps[0] if context.apps else ""
    for app in context.apps:
        app_title, _ = get_app_title_and_version(app)
        context.app_titles[app] = app_title
