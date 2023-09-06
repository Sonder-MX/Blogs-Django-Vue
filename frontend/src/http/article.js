import request from "."

// 获取文章列表
export const getArticleList = (page) => {
  if (page <= 1) {
    page = 1
  }
  return request.get("/article/?page=" + page)
}

// 根据id获取文章
export const getArticleById = (articleId) => request.post(`/article/${articleId}/`)
