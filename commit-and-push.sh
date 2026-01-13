#!/bin/bash
cd /workspaces/bdgamble-skills-build-applications-w-copilot-agent-mode
git add -A
git commit -m "Add React frontend with Bootstrap styling and OctoFit branding

- Created all React components (Teams, Users, Activities, Workouts, Leaderboard)
- Implemented REST API integration with Django backend
- Added vibrant purple/blue gradient styling with App.css
- Integrated OctoFit logo in navbar with animations
- Updated favicon and page title
- Added responsive Bootstrap tables, cards, and buttons
- Included loading spinners for better UX
- Configured environment variable support for Codespaces URLs
- Added console logging for debugging API calls
- Handled both paginated and plain array API responses"
git push origin build-octofit-app
echo "Changes committed and pushed successfully!"
