const fetch = require("node-fetch");

const API_TOKEN = process.env.API_TOKEN;
const COMMUNITY_ID = process.env.COMMUNITY_ID;
const CIRCLE_COMMUNITY_PATH = process.env.CIRCLE_COMMUNITY_PATH;
const BEGGINER_SPACE_ID = process.env.BEGGINER_SPACE_ID;
const MEDIUM_SPACE_ID = process.env.MEDIUM_SPACE_ID;
const ADVANCED_SPACE_ID = process.env.ADVANCED_SPACE_ID;

const postQuestion = async (question) => {
	const { title, difficulty, body, author_email } = question;

	console.log(difficulty);
	const requestOptions = {
		method: "POST",
		headers: { Authorization: API_TOKEN },
	};

	const questionDifficulties = {
		Beginner: BEGGINER_SPACE_ID,
		Medium: MEDIUM_SPACE_ID,
		Advanced: ADVANCED_SPACE_ID,
	};

	const SPACE_ID = questionDifficulties[difficulty];

	//url creation
	const post_url = `${CIRCLE_COMMUNITY_PATH}/api/v1/posts?community_id=${COMMUNITY_ID}&SPACE_ID=${SPACE_ID}&`;
	const post_title = `name=${title}&`;
	const post_body = `body=${body}&`;
	const post_url_ending_params = `is_comments_enabled=true&is_liking_enabled=true&is_truncation_disabled=true`;
	const post_author = `&user_email=${author_email}`;

	const url_pieces = [post_url, post_title, post_body, post_url_ending_params];
	if (author_email) {
		url_pieces.append(post_author);
	}
	const url = encodeURI(url_pieces.join(""));

	await fetch(url, requestOptions)
		.then((response) => response.json())
		.then((result) => {
			console.log(result);
		})
		.catch((error) => console.log("error", error));
};

module.exports = { postQuestion };
