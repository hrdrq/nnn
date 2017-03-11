var app = new Vue({
  el: '#app',
  data: {
    word: '',
    platforms: [
      {
        name: 'shopee',
        logo: 'shopee.png',
        results: null,
        country: 'tw'
      },
      // {
      //   name: 'ruten',
      //   logo: 'ruten.png',
      //   results: null,
      //   country: 'tw'
      // },
      {
        name: 'yahoo_tw',
        logo: 'yahoo_tw.png',
        results: null,
        country: 'tw'
      },
      {
        name: 'yahoo_jp',
        logo: 'yahoo_jp.png',
        results: null,
        country: 'jp'
      },
      // {
      //   name: 'mercari',
      //   logo: 'mercari.png',
      //   results: null,
      //   country: 'jp'
      // },
      {
        name: 'rakuma',
        logo: 'rakuma.png',
        results: null,
        country: 'jp'
      },
      {
        name: 'amazon',
        logo: 'amazon.png',
        results: null,
        country: 'jp'
      },
    ],
    rate: null,
  },
  mounted () {
    root = this
    $.ajax({
        type: 'GET',
        url: API_HOST + 'rate',
        contentType:'application/json',
    })
    .done(function (res, ts, j) {
      root.rate = res.rate
    });
  },
  methods: {
    search: function () {
      if(this.word == '')return;
      root = this
      root.platforms.forEach(function (platform){
        platform.results = null;
        $.ajax({
          type: 'GET',
          url: API_HOST + 'price',
          contentType:'application/json',
          data: {
            word: root.word,
            platform: platform.name,
          }
        })
        .done(function (res, ts, j) {
          platform.results = res.results;
        });
      });
    },
  }
})
