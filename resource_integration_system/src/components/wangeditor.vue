<template>
    <div>
      <div id="editor">
          <div style="border: 1px solid #ccc">
              <Toolbar
                  style="border-bottom: 1px solid #ccc"
                  :editor="editorRef"
                  :mode="mode"
              />
              <Editor
                  style="height: auto; overflow-y: hidden;"
                  :modelValue="modelValue"
                  :defaultConfig="editorConfig"
                  :mode="mode"
                  @onCreated="handleCreated"
                  @onChange="handleChange"
              />
          </div>
      </div>
    </div>
  </template>
  
  <script>
  import '@wangeditor/editor/dist/css/style.css'
  import { onBeforeUnmount, shallowRef, watch } from 'vue'
  import { Editor, Toolbar } from '@wangeditor/editor-for-vue'
  
  export default {
    name: 'wangeditor',
    components: { Editor, Toolbar },
    props: {
      modelValue: {
        type: String,
        default: ''
      }
    },
    emits: ['update:modelValue'],
    setup(props, { emit }) {
      const editorRef = shallowRef()
      const mode = 'default'
      
      const editorConfig = { 
        MENU_CONF: {
          uploadImage: {
            headers: {},
            server: process.env.VUE_APP_BASE_API + "/public/fileupload/4564",
            fieldName: 'file',
          }
        }
      }
  
      const handleCreated = (editor) => {
        editorRef.value = editor
        // 初始化设置编辑器内容
        editor.setHtml(props.modelValue)
      }
  
      // 监听内容变化
      const handleChange = (editor) => {
        const html = editor.getHtml()
        emit('update:modelValue', html)
      }
  
      // 监听外部传入的modelValue变化
      watch(() => props.modelValue, (newVal) => {
        if (editorRef.value && newVal !== editorRef.value.getHtml()) {
          editorRef.value.setHtml(newVal)
        }
      })
  
      onBeforeUnmount(() => {
        const editor = editorRef.value
        if (editor == null) return
        editor.destroy()
      })
  
      return {
        editorRef,
        mode,
        editorConfig,
        handleCreated,
        handleChange
      }
    }
  }
  </script>