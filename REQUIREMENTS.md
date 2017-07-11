# VITA App Backend Requirements
VITA will be launching apps and web pages to help support their tax preparation services.

## 1. RESTful Web Services

### 1.1 Site Management
#### 1.1.1 Create Site
- PUT /vita/<version>/site

#### 1.1.2 Get Site Details
- GET /vita/<version>/site/<sitename>

#### 1.1.2 Update Site Status
- POST /vita/<version>/site/<sitename>

#### 1.1.3 Get Site List
- GET /vita/<version>/site

### 1.2 User and Role Management

#### 1.2.1 Create New User
- PUT /vita/<version>/user

#### 1.2.2 Update User Roles
- POST /vita/<version>/user/<userid>

#### 1.2.3 Log In User
- PUT /vita/<version>/session

#### 1.2.4 Log Out User
- DELETE /vita/<version>/session

# 2. Technical Details
The requirements point to three data structures: a Site, User, and Session.

## 2.1 Site Model
| Field | Data Type | Default Value |
| ------------- | --------- | ------------- |
| Site Name     | String    |  <required>   |
| Site Address  | String    |  <required>   |
| Site Hours    | String    |  "9-5"        |
| Is Site Open? | Boolean   |  False        |
| Site Availability | String | Enum { Red Yellow Green }, Default "Green" |

## 2.2 User Model
| Field | Data Type | Default Value |
| ------------- | --------- | ------------- |
| User Email    | String    |  <required>, <unique>   |
| Password      | String    |  <required>   |
| Roles         | Array of String | Enum { 'New User', 'Site Coordinator', 'Admin', 'Site Coordinator, Inactive' }, Default 'New User' |

