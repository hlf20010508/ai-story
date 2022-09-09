import Mock from "mockjs";
//Mock.mock("url", "get/post", require("file"));
//Mock.mock("url", "post", (request) => { console.log("request: ", request) });
Mock.mock("/api/getOutput?beginText=test", "get", require("../../static/story.json"));