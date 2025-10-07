<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="F2"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 04:41:26 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6NTI6MDcgUE07MjU3Nw=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6NDE6MjYgUE07NDsyNjg5"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Coffee, Tea, Menu, Qty" type="Integer" array="False" size=""/>
            <assign variable="Coffee" expression="25"/>
            <assign variable="Tea" expression="20"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;Select menu&quot;" newline="True"/>
            <output expression="&quot;1. Coffee&quot;" newline="True"/>
            <output expression="&quot;2. Tea&quot;" newline="True"/>
            <input variable="Qty"/>
            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
            <input variable="Menu"/>
            <if expression="Menu==1">
                <then>
                    <if expression="Qty = 10">
                        <then>
                            <output expression="&quot;Baht = 25 &quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Enter quantity:99&quot;" newline="True"/>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                    <output expression="Coffee" newline="True"/>
                </then>
                <else>
                    <if expression="Menu==2">
                        <then>
                            <output expression="&quot;Baht = 20 &quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;sold out&quot;" newline="True"/>
                        </else>
                    </if>
                    <output expression="&quot;Sold out&quot;" newline="True"/>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>