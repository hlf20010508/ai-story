<template>
  <div class="index">
    <el-row>
      <h1 class="index-title">中文文章续写系统</h1>
    </el-row>
    <el-row>
      <el-form :inline="true" class="index-form">
        <el-form-item class="index-begin-text" label="开头">
          <el-input
            class="index-input"
            v-model="beginText"
            placeholder="请输入文章的开头"
            :clearable="true"
            @keyup.enter.native="getOutput"
            >\
            <i class="el-icon-edit" slot="prefix"></i>
          </el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="getOutput">生成</el-button>
        </el-form-item>
      </el-form>
    </el-row>
    <el-row>
      <el-divider class="index-divider"></el-divider>
    </el-row>
    <el-row>
      <div class="index-output">
        <p class="index-output-text">
          {{ output }}
        </p>
      </div>
    </el-row>
    <el-row v-if="hasCreated">
      <el-col :span="12">
        <div class="index-time-span">
          <span>
            续写耗时：
            <span class="index-time">{{ time }}s</span>
          </span>
        </div>
      </el-col>
      <el-col :span="12">
        <div class="index-another" @click="getOutput">
          <span>
            <i class="el-icon-refresh"></i>
            换一个
          </span>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      beginText: "",
      output: "",
      hasCreated: false,
      time: 0,
    };
  },
  methods: {
    getOutput() {
      let loading = this.$loading()
      this.axios
        .get("/api/getOutput", {
          params: {
            beginText: this.beginText,
          },
        })
        .then((res) => {
          console.log(res.data);
          if (res.data.success) {
            this.output = res.data.output;
            this.time = res.data.time;
            this.hasCreated = true;
          } else {
            alert("提交失败");
            this.hasCreated = false;
          }
          loading.close()
        });
    },
  },
};
</script>

<style>
.index {
  width: 100%;
  margin-top: 20%;
}
.index-title {
  background: url("/static/title-green.png") no-repeat;
  background-size: 100% 100%;
  color: #ffffff;
}
.index-form {
  height: 50px;
}
.index-input .el-input__inner {
  padding-left: 28px;
}
.index-input .el-input__prefix {
  margin-left: 4px;
}
.index-begin-text .el-form-item__label {
  background: url("/static/title-grey.png") no-repeat;
  background-size: 100% 100%;
  padding: 0 8px;
  margin-right: 8px;
  color: #ffffff;
}
.index-divider {
  margin: 14px 0;
}
.index-output {
  background: url("/static/frame.png") no-repeat;
  background-size: 100% 100%;
  min-height: 110px;
  padding: 12px 0;
}
.index-output-text {
  text-align: left;
  margin: 0 auto;
  padding: 10px 40px;
  font-weight: bold;
  font-size: 22px;
  color: #2f2f2f;
}
.index-time {
  color: #846e4e;
  font-weight: bold;
}
.index-time-span {
  text-align: left;
}
.index-another {
  text-align: right;
}
.index-another:hover {
  color: #377219;
  cursor: pointer;
}
</style>