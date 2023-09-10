<template>
    <el-dialog :visible.sync="isShow" top='0px'>
      <el-image style="width: 100%; height: 100%" :src="this.imgSrc"></el-image>
    </el-dialog>
</template>

<script>
export default {
  props: {
    show: Boolean,
    imgSrc: String
  },
  computed: {
    isShow: {
      get() {
        return this.show
      },
      set(val) {
        this.$emit('update:show', val)
      }
    }
  }
}
</script>
