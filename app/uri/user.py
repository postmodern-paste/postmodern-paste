from uri.base_uri import URI


class UserLoginInterfaceURI(URI):
    path = '/login'


class UserLogoutInterfaceURI(URI):
    path = '/logout'


class UserRegisterInterfaceURI(URI):
    path = '/register'


class UserAccountInterfaceURI(URI):
    path = '/account'


class UserCreateURI(URI):
    api_endpoint = True
    path = '/api/user/create'


class UserUpdateDetailsURI(URI):
    api_endpoint = True
    path = '/api/user/update'


class UserDeactivateURI(URI):
    api_endpoint = True
    path = '/api/user/deactivate'


class UserAPIKeyRegenerateURI(URI):
    api_endpoint = True
    path = '/api/user/api_key/regenerate'


class CheckUsernameAvailabilityURI(URI):
    api_endpoint = True
    path = '/api/user/check_username_availability'


class ValidateEmailAddressURI(URI):
    api_endpoint = True
    path = '/api/user/validate_email_address'
