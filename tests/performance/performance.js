import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = {
    duration: '1m',
    vus: 5,
    thresholds: {
        http_req_duration: ['p(95)<500']
    },
};
export default function () {
    let res = http.get(`${__ENV.API_ENDPOINT}/test/getHello?lang=en`, { tags: { name: '01_Home' } });
    check(res, {
        'is status 200': (r) => r.status === 200,
    });
    sleep(Math.random() * 5);
}