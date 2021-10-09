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