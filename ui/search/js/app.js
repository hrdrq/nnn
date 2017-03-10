INITIAL_DATA = 
{
  word: 'EOS 5D Mark IV',
  rate: null,
  tw_res: null,
  jp_res: null,
  tw_select: null,
  jp_select: null,
  profit: null,
}

var app = new Vue({
  el: '#app',
  data: {
    data: Object.assign({}, INITIAL_DATA),
  },
  mounted () {
    root = this
    $.ajax({
        type: 'GET',
        url: API_HOST + 'rate',
        contentType:'application/json',
    })
    .done(function (res, ts, j) {
      root.data.rate = res.rate
    });
  },
  methods: {
    search: function () {
      root = this
      $.ajax({
          type: 'GET',
          url: API_HOST + 'price/feebee?word=' + this.data.word,
          contentType:'application/json',
      })
      .done(function (res, ts, j) {
        root.data.tw_res = res.results;
        root.data.tw_select=0
        root.profit_calc();
      });
      $.ajax({
          type: 'GET',
          url: API_HOST + 'price/kakaku?word=' + this.data.word,
          contentType:'application/json',
      })
      .done(function (res, ts, j) {
        root.data.jp_res = res.rows;
        root.data.jp_select=0
        root.profit_calc();
      });
    },
    profit_calc: function () {
      if(this.data.tw_select==null || this.data.jp_select==null || this.data.rate==null) return;
      tw_product = this.data.tw_res[this.data.tw_select];
      if(tw_product.price.length == 1){
        tw_price = parseInt(tw_product.price[0].toString().replace(',',''))
      }else if(tw_product.price.length == 2){
        tw_price = (parseInt(tw_product.price[0].toString().replace(',','')) + parseInt(tw_product.price[1].toString().replace(',','')))/2
      }
      jp_product = this.data.jp_res[this.data.jp_select];
      jp_price = jp_product.price

      this.data.profit = parseInt(tw_price - (jp_price/this.data.rate))
    }
  }
})
