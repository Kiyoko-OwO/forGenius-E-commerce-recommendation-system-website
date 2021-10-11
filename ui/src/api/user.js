import request from '../utils/request'

export const login = data => {
    return request({
      method: 'POST',
      url: 'user/login/',
      data
    })
}
export const signup = data => {
    return request({
      method: 'POST',
      url: 'user/register/',
      data
    })
}
export const change_password = data => {
  return request({
    method: 'POST',
    url: 'user/change_password/',
    data
  })
} 

export const address_view = data => {
  return request({
    method: 'POST',
    url: 'user/address/view/',
    data
  })
}

export const logout = data => {
  return request({
    method: 'POST',
    url: 'user/logout/',
    data
  })
}

export const address_delete = data => {
  return request({
    method: 'DELETE',
    url: '/user/address/delete/',
    data
  })
}

export const interest_add = data => {
  return request({
    method: 'POST',
    url: '/user/interests/add/',
    data
  })
}