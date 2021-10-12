import request from '../utils/request'

export const product_view = parameter => {
    return request({
      method: 'GET',
      url: '/product/user/view/',
      params: parameter
    })
}