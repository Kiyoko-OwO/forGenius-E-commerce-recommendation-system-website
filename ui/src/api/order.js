import request from '../utils/request'

export const car_add = data => {
    return request({
      method: 'POST',
      url: '/order/cart/add/',
      data
    })
}