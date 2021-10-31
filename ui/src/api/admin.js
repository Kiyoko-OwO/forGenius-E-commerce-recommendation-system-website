import request from '../utils/request'

export const admin_view = data => {
    return request({
      method: 'POST',
      url: '/product/all/',
      data
    })
  }

  export const product_add = data => {
    return request({
      method: 'POST',
      url: '/product/add/',
      data
    })
  }