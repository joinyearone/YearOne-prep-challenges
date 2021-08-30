const fetch = require("node-fetch");

const postQuestion = async (question, questionNumber) => {
	const { title, difficulty, source, body, author_name } = question;

	console.log(body);
	console.log(title);
	// author_email.join("");
	console.log(difficulty);

	const requestOptions = {
		method: "POST",
		headers: { Authorization: `eefCFAfzz3yAZZUfBdw2Ba2M` },
	};

	const questionDifficulties = {
		Beginner: 140192,
		Medium: 140193,
	};

	let space_id = questionDifficulties[difficulty];

	let community_id = 11548;

	//post sections
	let urlTitle = `Interview Prep Challenge #${questionNumber}: ${title}&`;
	let urlBody = `
  👏👏 Thanks to ${author_name} for the question!👏👏<br>
  <strong>Difficulty Level:</strong> ${difficulty}<br>
  <strong>Sourced from:</strong> ${source}<br>
  ${body}
  &`;

	const url = formatPostBody(urlTitle, urlBody);
	//url creation
	function formatPostBody(title, body) {
		const post_url = `https://app.circle.so/api/v1/posts?community_id=${community_id}&space_id=${space_id}&`;
		const post_title = `name=${title}&`;
		const post_body = `internal_custom_html=${body}&`;
		const post_url_ending_params = `is_comments_enabled=true&is_liking_enabled=true&is_truncation_disabled=false`;

		const url_pieces = [
			post_url,
			post_title,
			post_body,
			post_url_ending_params,
		];

		console.log(post_title);
		console.log(post_body);
		return encodeURI(url_pieces.join(""));
	}
	console.log({ url });

	await fetch(url, requestOptions)
		.then((response) => response.json())
		.then((result) => {
			console.log(result.success);
			// console.log({ result });
		})
		.catch((error) => console.log("error", error));
};

module.exports = { postQuestion };

// const API_TOKEN = process.env.API_TOKEN;
// const COMMUNITY_ID = process.env.COMMUNITY_ID;
// const CIRCLE_COMMUNITY_PATH = process.env.CIRCLE_COMMUNITY_PATH;
// const BEGGINER_SPACE_ID = process.env.BEGGINER_SPACE_ID;
// const MEDIUM_SPACE_ID = process.env.MEDIUM_SPACE_ID;
// const ADVANCED_SPACE_ID = process.env.ADVANCED_SPACE_ID;

// const postQuestion = async (question) => {

// const { title, difficulty, body, author_email } = question;

// console.log(difficulty);
// const requestOptions = {
//   method: "POST",
//   headers: { Authorization: API_TOKEN },
// };

// const questionDifficulties = {
//   Beginner: BEGGINER_SPACE_ID,
//   Medium: MEDIUM_SPACE_ID,
//   Advanced: ADVANCED_SPACE_ID,
// };

// const SPACE_ID = questionDifficulties[difficulty];

// // url creation
// const post_url = `${CIRCLE_COMMUNITY_PATH}/api/v1/posts?community_id=${COMMUNITY_ID}&SPACE_ID=${SPACE_ID}&`;
// const post_title = `name=${title}&`;
// const post_body = `body=${body}&`;
// const post_url_ending_params = `is_comments_enabled=true&is_liking_enabled=true&is_truncation_disabled=true`;
// const post_author = `&user_email=${author_email}`;

// const url_pieces = [post_url, post_title, post_body, post_url_ending_params];
// if (author_email) {
//   url_pieces.append(post_author);
// }
// const url = encodeURI(url_pieces.join(""));

// await fetch(url, requestOptions)
//   .then((response) => response.json())
//   .then((result) => {
//     console.log(result);
//   })
//   .catch((error) => console.log("error", error));
// };

// module.exports = { postQuestion };
