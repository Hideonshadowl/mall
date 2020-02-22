<template>
    <div class="shopcart-box">
        <div style="margin-bottom: 3rem;width: 100%">
        <div v-for="item in this.$store.state.shopcartlist" style="border-bottom: 5px solid #dcdcdc">
          <i style="margin-left: 4rem;font-size: 0.4rem"> {{item[0].name}}</i>
          <img :src=item[0].img_url alt="" style="height: 40%;width: 40%">
          <span style="font-size: 0.4rem;color: red">{{item[0].price}}¥ </span>* {{item[1]}}
          <i class="el-icon-minus" @click="reduce(item)" style="display: inline-block;margin-left: 1.5rem"></i>
          <i class="el-icon-plus" @click="add(item)" style="display: inline-block;margin-left: 0.1rem"></i>
          <i class="el-icon-delete" @click="deletethis(item)" style="display: inline-block;margin-left: 0.8rem"></i>
        </div>
        </div>
      <div>
        <p style="background: #e8e8e8;height: 1.5rem;position: fixed;width: 50%;z-index: 1001;left: 0;bottom:1.5rem;font-size: 0.5rem;line-height: 1.4rem;">合计: {{totalprice}}￥</p>
        <p style="background: goldenrod;height: 1.5rem;position: fixed;width: 50%;z-index: 1001;left: 5rem;bottom:1.5rem;font-size: 0.5rem;text-align: center;line-height: 1.4rem" @click="topay()">结算</p>
      </div>
      <navBar></navBar>
    </div>
</template>

<script>
    import navBar from '../../components/navBar'
    import {mapState,mapActions} from 'vuex'

    export default {
        data() {
            return {
                cartProductVoList: '',
                totalprice:0

            }
        },

        created() {
          this.compute_total_price()

        },
        mounted(){
        },
        methods: {
          ...mapActions(['reducecount','addcount','deleteone']),
          deletethis(val){
              this.deleteone(val);
              this.$forceUpdate();
              this.compute_total_price();
          },
          reduce(val) {
              console.log('fuck');
              this.reducecount(val);
              this.$forceUpdate();
              this.compute_total_price();
              console.log('finish');
          },

          add(val) {
              console.log('fuck');
              this.addcount(val);
              this.$forceUpdate();
              this.compute_total_price();
              console.log('finish');
          },
          compute_total_price(){
              this.totalprice=0;
              this.$store.state.shopcartlist.forEach(value => {
              this.totalprice+=value[0].price*value[1]
            });
          },
          topay(){this.$router.push({
            path:'./order',
            query:{
              totalprice:this.totalprice
            }
          })}

        },

        components: {
          navBar,
        }
    }
</script>

<style lang="scss" scoped="" type="text/scss">

</style>
