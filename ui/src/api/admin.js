import request from '../utils/request'

export const car_view = parameter => {
    return request({
      method: 'GET',
      url: '/order/cart/view/',
      params: parameter
    })
  }

  export const product_add = data => {
    return request({
      method: 'POST',
      url: '/product/add/',
      data
    })
  }