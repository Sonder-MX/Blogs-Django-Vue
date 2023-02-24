import axios from "axios"

const tagUrl = "http://127.0.0.1:8000/api"

export const reqArticleListOrDetail = async (resUrl) => {
  const response = await axios.get(tagUrl + resUrl)
  return response.data
}
