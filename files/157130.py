<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_2"/>
        <attribute name="authors" value="Admin"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 05:56:31 PM"/>
        <attribute name="created" value="QWRtaW47Q0FSTEFSOzI1NjgtMDctMTY7MDU6Mzc6MjEgUE07MjIyMw=="/>
        <attribute name="edited" value="QWRtaW47Q0FSTEFSOzI1NjgtMDctMTY7MDU6NTY6MzEgUE07NjsyMzM4"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <declare name="Coffee, Tea, menu, q, total" type="Integer" array="False" size=""/>
            <assign variable="Coffee" expression="25"/>
            <assign variable="Tea" expression="20"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
            <input variable="q"/>
            <if expression="menu == 1">
                <then>
                    <if expression="q &lt;= 10">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <assign variable="total" expression="Coffee * q"/>
                            <output expression="&quot;Total Price : &quot;&amp;total&amp; &quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="menu == 2">
                        <then>
                            <if expression="q &lt;= 0">
                                <then>
                                    <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                                    <assign variable="total" expression="Tea * q"/>
                                    <output expression="&quot;Total Price : &quot;&amp;total&amp; &quot;Baht&quot;" newline="True"/>
                                    <output expression="&quot;Enjoy!&quot;" newline="True"/>
                                </then>
                                <else>
                                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                                </else>
                            </if>
                        </then>
                        <else/>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>