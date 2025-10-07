<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_1.2"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 04:51:42 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6MzQ6NDAgUE07MjU3Ng=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6NTE6NDIgUE07MTsyNjg1"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="c, t, m, eq, tp" type="Integer" array="False" size=""/>
            <assign variable="c" expression="25"/>
            <assign variable="t" expression="20"/>
            <output expression="&quot;Beverage List: &quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty:10 &quot;" newline="True"/>
            <output expression="&quot;2.Tea - 20 Baht - Qty:0 &quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="m"/>
            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
            <input variable="eq"/>
            <if expression="m==2">
                <then>
                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                </then>
                <else>
                    <if expression="eq&gt;10">
                        <then>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <assign variable="tp" expression="c*eq"/>
                            <output expression="&quot;Total Price : &quot;&amp;tp&amp; &quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>