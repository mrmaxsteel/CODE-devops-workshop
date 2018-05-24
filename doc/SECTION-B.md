# Workshop
## Section B: Configure your Jenkins Master
### Step B.1: Configure Security
From GitHub.com:
* Click on your profile in the top right and select 'Settings'
* Choose 'Developer Settings', then chose 'New OAuth App':
  * Application: Jenkins-AWS
  * Homepage URL: "http://<PUBLIC_DNS_NAME>:8080/"
  * Authorization callback URL: "http://<PUBLIC_DNS_NAME>:8080/securityRealm/finishLogin"
* Click 'Register Application', copy the 'Client ID' and 'Client Secret'

From the Jenkins Web UI:
* Choose Manage Jenkins > Configure Global Security. Check 'Enable Security'
* Under 'Security Realm', Select 'GitHub Authentication Plugin'. Keep the defaults, but paste the Client ID and Client Secret you created above
* Under 'Authorization', Select 'GitHub Committer Authorization Strategy':
  * **IMPORTANT:** In the "Admin User Names" field, enter your GitHub user name. Be sure to get it exactly right!
  * Check 'Use GitHub repository permissions'
* Select 'Save'. This will refresh the window and try to reconnect to Jenkins using your GitHub Credentials. Select 'Authorize', and you should now be logged into Jenkins using your GitHub account!
### Step B.2: Configure WebHooks
From GitHub.com:
* Create a GitHub Personal Access Token: 
  * Go to https://github.com/settings/tokens and 'Generate New Token'
  * Call the token something like "Jenkins"
  * Select the following scopes: repo, admin:repo_hook, user
  * Click "Generate Token", copy the token and keep it safe

From the Jenkins Web UI:
* Choose 'Credentials', under 'Domains', click "(global)"
* Add a Credential:
  * Kind: Username with Password
  * Scope: Global
  * Username: \<your GitHub username\>
  * Password: \<PAToken generated above\>
  * ID: GITHUB_PATOKEN_USERPASS
  * Description: GITHUB_PATOKEN_USERPASS
* Add a second Credential:
  * Kind: Secret Text
  * Scope: Global
  * Secret: \<PAToken generated above\>
  * ID: GITHUB_PATOKEN_SECRET
  * Description: GITHUB_PATOKEN_SECRET
* Go to Jenkins > Manage Jenkins > Configure System
* Scroll down to GitHub, under GitHub Servers, choose 'Add GitHub Server':
  * Under 'Name', enter "GitHub"
  * Select GITHUB_PATOKEN_SECRET from the 'Credentials' drop-down
* Check 'Manage Hooks'
* 'Test Connection'. If successful, 'Save' the configuration
### Step B.3: Set up a Multibranch Pipeline
* From GitHub, take a 'Fork' of this repository.
* From the Jenkins UI, choose 'create new jobs' or 'New Item'
* Pick a name, e.g. "CODE-devops-workshop", select 'Multibranch Pipeline', and press OK
* Under Branch Sources, 'Add Source' > 'GitHub':
  * Credentials: GITHUB_PATOKEN_USERPASS
  * Owner: \<Your GitHub Username\>
  * Repository: CODE-devops-workshop
  * Discovery Branches Strategy: All branches
  * Leave 'Discover PRs from origin' and delete 'Discover PRs from forks' by pressing the red X
  * 'Add' > 'Filter by name (with wildcards)'. In the 'Include' field, enter: "master PR*"
* Select 'Save'  