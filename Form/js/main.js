var app = new Vue({
  el: '#app',
  data: {
    lyrics: '',
    genero: '',
    url_destino: 'http://127.0.0.1:5000/', // Variável que indica o endereço do servidor
    show_alert: false
  },
  methods: {
    request: function() {

      // Se não tiver nada na text area, mostra alerta e retorna
      if(this.lyrics == ''){
        this.show_alert = true
        return
      }
      else{
        this.show_alert = false
      }


      this.genero = ''
      var self=this
      // Criando JSON para envio
      var str = this.lyrics
      var json = {"Lyrics": str}
      json = JSON.stringify(json)
      console.log(json)

      this.$http.post(self.url_destino,json).then(function(response){
        if(response.status == "200"){
            console.log('Resposta Recebida!  ' + response.data[0]);
          resp = response.data[0]
          if(resp == 0){
            self.genero = 'Bossa Nova'
          }
          else if(resp == 1){
            self.genero = 'Funk'
          }
          else if(resp == 2){
            self.genero = 'Gospel'
          }
          else if(resp == 3){
            self.genero = 'Sertanejo'
          }
          else{
            self.genero = ''
          }

        }
      })
    },

    hide_alert: function(){
      this.show_alert = false
    }
  }
})
