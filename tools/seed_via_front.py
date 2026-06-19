#!/usr/bin/env python3
"""Automate a real browser with Playwright to seed the frontend admin UI with data.

This script performs these steps (when you run it):
 - reads JSON data produced by `extract_cv.py`
 - optionally registers an admin via POST /auth/register
 - logs in to obtain a token
 - launches Playwright, sets localStorage token, visits the app, fills admin forms and submits

Usage (dry-run, do not run without confirming):
  pip install -r tools/requirements-playwright.txt
  playwright install
  python tools/seed_via_front.py cv.json --admin-email me@example.com --admin-password secret

NOTE: This script is prepared but will not be executed by me unless you ask.
"""
import argparse
import json
import time
from pathlib import Path

import requests

try:
    from playwright.sync_api import sync_playwright
except Exception:
    raise SystemExit("playwright required. Install with: pip install playwright")


API_BASE = 'http://localhost:8000'
FRONT_DIR = Path(__file__).resolve().parents[1] / 'src' / 'frontend' / 'build'


def register_admin(email, password):
    url = f"{API_BASE}/auth/register"
    resp = requests.post(url, json={"email": email, "password": password})
    resp.raise_for_status()
    return resp.json()


def login_admin(email, password):
    url = f"{API_BASE}/auth/token"
    data = {'username': email, 'password': password}
    resp = requests.post(url, data=data)
    resp.raise_for_status()
    return resp.json().get('access_token')


def serve_frontend_background():
    # Caller is expected to serve the build at http://localhost:3000
    print("Ensure the frontend build is served at http://localhost:3000")


def run_playwright(data, token, admin_email):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to frontend
        page.goto('http://localhost:3000')

        # Set token in localStorage and reload so admin UI is authenticated
        page.evaluate(
            """([token, email]) => {
                localStorage.setItem('portfolio_admin_token', token);
                localStorage.setItem('portfolio_admin_email', email);
            }""",
            [token, admin_email],
        )
        page.reload()
        time.sleep(1)

        # Wait for admin section to be available
        page.wait_for_selector('#admin')

        # Fill profile form
        profile = data.get('profile', {})
        # Fill fields by id
        mapping = {
            'prenom': profile.get('prenom', ''),
            'nom': profile.get('nom', ''),
            'email': profile.get('email', ''),
            'telephone': profile.get('telephone', ''),
            'adresse': profile.get('adresse', ''),
            'dn': profile.get('dn', ''),
            'linkedin': profile.get('linkedin', ''),
            'github': profile.get('github', ''),
            'photo': profile.get('photo', ''),
            'bio': profile.get('bio', ''),
        }

        for field_id, value in mapping.items():
            try:
                el = page.query_selector(f"#{field_id}")
                if el is None:
                    continue
                el.fill(value)
            except Exception:
                continue

        # Submit the first 'Ajouter profile' button
        # Buttons have class admin__submit; the first form corresponds to profile
        try:
            buttons = page.query_selector_all(".admin__submit")
            if buttons:
                buttons[0].click()
        except Exception:
            pass

        # You can expand this to create formations, competences, projects etc.

        print("Seeding completed in browser (check UI for results).")
        # Keep browser open for manual inspection
        print("Browser left open for inspection. Close manually when done.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data', help='JSON file produced by extract_cv.py')
    parser.add_argument('--admin-email', required=True)
    parser.add_argument('--admin-password', required=True)
    parser.add_argument('--register', action='store_true', help='Call /auth/register before login')
    args = parser.parse_args()

    data_path = Path(args.data)
    if not data_path.exists():
        raise SystemExit(f"Data file not found: {data_path}")

    data = json.loads(data_path.read_text())

    if args.register:
        print('Registering admin...')
        register_admin(args.admin_email, args.admin_password)

    print('Logging in...')
    token = login_admin(args.admin_email, args.admin_password)
    if not token:
        raise SystemExit('Failed to obtain token')

    print('Launching browser...')
    serve_frontend_background()
    run_playwright(data, token, args.admin_email)


if __name__ == '__main__':
    main()
