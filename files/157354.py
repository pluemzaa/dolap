<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="sigma"/>
        <attribute name="authors" value="ITSeed"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-17 06:22:06 PM"/>
        <attribute name="created" value="SVRTZWVkO0RFU0tUT1AtOEFBRU9QMjsyMDI1LTA3LTE3OzA2OjAwOjExIFBNOzI4NjU="/>
        <attribute name="edited" value="SVRTZWVkO0RFU0tUT1AtOEFBRU9QMjsyMDI1LTA3LTE3OzA2OjIyOjA2IFBNOzE7Mjk4MQ=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="menu, coffeePrice, coffeeQty, quantity, total" type="Integer" array="False" size=""/>
            <assign variable="coffeePrice" expression="25"/>
            <assign variable="coffeeQty" expression="10"/>
            <output expression="&quot;Baverage List&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="menu"/>
            <if expression="menu ==1">
                <then>
                    <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                    <input variable="quantity"/>
                    <if expression="quantity &lt;=10 and quantity &gt;0">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price:&quot;&amp;coffeePrice&quot;quantity&amp; &quot; baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="menu ==2">
                        <then>
                            <output expression="&quot;Enter quantity&quot;" newline="True"/>
                            <input variable="quantity"/>
                        </then>
                        <else/>
                    </if>
                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>