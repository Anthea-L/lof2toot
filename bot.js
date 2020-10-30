require('dotenv').config();
const Mastodon = require('mastodon-api');
const fs = require('fs')

console.log("Mastodonbot starting....");


const M = new Mastodon({
  client_key: process.env.CLIENT_KEY,
  client_secret: process.env.CLIENT_SECRET,
  access_token: process.env.ACCESS_TOKEN,
  timeout_ms: 60*1000,  // optional HTTP request timeout to apply to all requests.
  api_url: 'https://obkkszd.club/api/v1/', // optional, defaults to https://mastodon.social/api/v1/
})

const postxt = fs.readFileSync('scraped_text.txt', (err, data) => { 
  if (err) throw err; 
  console.log(data.toString()); 
});

console.log(postxt);

toot();

function toot() {
  const params = {
    spoiler_text: "本日tag整理",
    status: postxt
  }

M.post('statuses', params, (error, data) => {
  if (error) {
    console.error(error);
  } else {
    //fs.writeFileSync('data.json', JSON.stringify(data, null, 2));
    //console.log(data);
    console.log(`ID: ${data.id} and timestamp: ${data.created_at}`);
    console.log(data.content);
  }
});
}
