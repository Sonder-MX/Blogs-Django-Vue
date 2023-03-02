import axios from "axios"

const tagUrl = "http://127.0.0.1:8000/api"

export const sendGetReq = async (resUrl) => {
  const response = await axios.get(tagUrl + resUrl)
  return response.data
}

export const sendPostReq = async (surl, payload, config_obj = "") => {
  return await axios.post(tagUrl + surl, payload, config_obj)
}

export const sendPutReq = async (surl, payload, config_obj) => {
  return await axios.put(tagUrl + surl, payload, config_obj)
}

export const sendPatchReq = async (surl, payload, config_obj) => {
  return await axios.patch(tagUrl + surl, payload, config_obj)
}

export const sendDeleteReq = async (surl, config_obj) => {
  return await axios.delete(tagUrl + surl, config_obj)
}
