<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="work_flowforithm_3"/>
        <attribute name="authors" value="Vivobook"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 07:18:45 PM"/>
        <attribute name="created" value="Vml2b2Jvb2s7TEFQVE9QLTFEODVNVU02OzI1NjgtMDctMTY7MDY6MjE6MDYgUE07MzE2OQ=="/>
        <attribute name="edited" value="Vml2b2Jvb2s7TEFQVE9QLTFEODVNVU02OzI1NjgtMDctMTY7MDc6MTg6NDUgUE07NDszMjkw"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="menu, quantity, Coffee, Tea, C, T, total" type="Integer" array="False" size=""/>
            <assign variable="Coffee" expression="25"/>
            <assign variable="Tea" expression="20"/>
            <assign variable="C" expression="10"/>
            <assign variable="T" expression="0"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
            <input variable="quantity"/>
            <if expression="menu == 1">
                <then>
                    <if expression="quantity &lt;= 10">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <assign variable="total" expression="quantity * Coffee"/>
                            <output expression="&quot;Total Price :&quot; &amp; total &amp; &quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="quantity == 0">
                        <then>
                            <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                            <assign variable="total" expression="quantity * Tea"/>
                            <output expression="&quot;Total Price :&quot; &amp; total &amp; &quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>