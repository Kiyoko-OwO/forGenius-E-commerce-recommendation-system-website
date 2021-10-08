import request from '../utils/request'

export const login = data => {
    return request({
      method: 'POST',
      url: 'login',
      data
    })
  }
export const signup = data => {
    return request({
      method: 'POST',
      url: 'signup',
      data
    })
  } 