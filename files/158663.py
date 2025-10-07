<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="rabbit"/>
        <attribute name="authors" value="prera"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 04:57:30 PM"/>
        <attribute name="created" value="cHJlcmE7UFJPR1JBTTsyNTY4LTA3LTIyOzEyOjA4OjA2IFBNOzIzNjc="/>
        <attribute name="edited" value="cHJlcmE7UFJPR1JBTTsyNTY4LTA3LTIyOzA0OjU3OjMwIFBNOzI7MjQ3OA=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="cofp, teap, cofqtn, teaqtn, qtn, menu, total" type="Integer" array="False" size=""/>
            <assign variable="cofqtn" expression="10"/>
            <assign variable="teaqtn" expression="0"/>
            <assign variable="cofp" expression="25"/>
            <assign variable="teap" expression="20"/>
            <output expression="&quot;Beverage List: &quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
            <input variable="qtn"/>
            <if expression="menu == 1">
                <then>
                    <if expression="qtn&lt;=10">
                        <then>
                            <assign variable="total" expression="cofp*qtn"/>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot;&amp;total&amp;&quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>