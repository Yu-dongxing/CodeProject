import request from '@/utils/request'

// 图书管理相关接口
export const BooksApi = {
  //分页查询图书/public/book/page?pageNum=1&pageSize=1
  findBookPage(page, size) {
    return request({
      url: `/public/book/page?pageNum=${page}&pageSize=${size}`,
      method: 'get'
    })
  },
  // 根据id查询图书
  findBookById(BookId) {
    return request({
      url: '/book/find/'+BookId,
      method: 'get'
    })
  },
  // 根据id删除图书
  deleteBookById(BookId) {
    return request({
      url: '/book/delete/'+BookId,
      method: 'delete'
    })
  },
}