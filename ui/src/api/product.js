import request from '../utils/request'

export const product_view = data => {
    return request({
      method: 'POST',
      url: '/product/user/view/',
      data
    })
}