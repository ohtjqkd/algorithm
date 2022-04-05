-- USING TABLE: COUPONS, CART_PRODUCTS
-- COUPONS: CART_ID, MINIMUM_REQUIRMENT, DISCOUNT_AMOUNT
-- CART_PRODUCTS: ID, CART_ID, ?, PRICE
-- SELECT CART_
-- 쿠폰은 원래 카트의 최소 구매 비용보다 높아야 사용이 가능하다. 하지만 버그 발생으로 최소 구매 비용보다 낮은 경우에도 쿠폰이 적용된거 같다.
-- 만약 해당 카트에 버그가 적용이 됐으면 1 아니면 0을 CART_ID와 함께 출력해라
-- 정렬은 CART_ID를 기준으로
SELECT COUPONS.CART_ID, IF(COUPONS.MINIMUM_REQUIREMENT > CART_SUM.SUMP, 1, 0) AS ABUSED 
        FROM COUPONS
        JOIN (SELECT CART_ID, SUM(PRICE) FROM CART_PRODUCTS GROUP BY CART_ID) AS CART_SUM
        ON COUPONS.CART_ID = CART_SUM.CART_ID
        ORDER BY COUPONS.CART_ID