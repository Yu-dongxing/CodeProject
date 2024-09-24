<!-- <template>
  <div class="CW">
    
  </div>
</template>

<script>
export default {
    name:"CwXt",


}
</script>

<style>
.CW{
    width: 150px;
    height: 150px;
    background-color: aqua;
}
</style> -->
<template>
  <div>
      <div class="tab-container">
        <button
          v-for="(tab, index) in tabs"
          :key="index"
          @click="changeTab(index)"
          :class="{ 'selected': currentTab === index }"
          class="tab-item"
          aria-selected="false"
        >
          {{ tab }}
          <div v-if="currentTab === index" class="underline"></div>
        </button>
      </div>
      <div class="content-container">
        <div v-for="(content, index) in contents" :key="index" v-show="currentTab === index">
          {{ content }}
        </div>
      </div>
    </div>
</template>

<script>
import { ref, onMounted } from 'vue'

export default {
  name: "CwXt",
  setup() {
    const tabs = ref(['Tab 1', 'Tab 2', 'Tab 3']);
    const contents = ref(['Content 1', 'Content 2', 'Content 3']);
    const currentTab = ref(0);

    function changeTab(index) {
      currentTab.value = index;
    }

    // 使用onMounted生命周期钩子来调用changeDisplay
    onMounted(() => {
      changeDisplay();
    });

    function changeDisplay() {
      var element = document.querySelector(".P_L");
      if (element) {
        element.style.display = "none";
      } else {
        console.log('没有找到指定类名的元素');
      }
    }

    return { tabs, contents, currentTab, changeTab, changeDisplay };
  }
}
</script>

<style>
.tab-container {
  display: flex;
}

.tab-item {
  cursor: pointer;
  margin-right: 20px;
  position: relative;
}

.tab-item.selected {
  font-weight: bold;
}

.underline {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: blue;
}

.content-container {
  margin-top: 20px;
}
</style>
