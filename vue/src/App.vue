<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: STKaiti;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 100%;
  max-width: 600px;
  height: 100%;
  margin: 0 auto 0 auto;
}
html,
body {
  margin: 0;
  height: 100%;
  background: url('/static/bg.png');
}
</style>
