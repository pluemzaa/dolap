<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab2"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 02:55:03 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6MTM6NTQgUE07MjU3Ng=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6NTU6MDMgUE07MzsyNjg2"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="cofpre, teapre, cofqtn, teaqtn, menu, qtn, total" type="Integer" array="False" size=""/>
            <assign variable="cofqtn" expression="10"/>
            <assign variable="teaqtn" expression="0"/>
            <assign variable="cofpre" expression="25"/>
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
                            <assign variable="total" expression="cofpre*qtn"/>
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