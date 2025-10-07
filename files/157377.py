<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="kkbs"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 11:54:44 PM"/>
        <attribute name="created" value="VXNlcjtERVNLVE9QLTNJQ0g4UUk7MjU2OC0wNy0xNzswOToyOTozOSBQTTsyNzgz"/>
        <attribute name="edited" value="VXNlcjtERVNLVE9QLTNJQ0g4UUk7MjU2OC0wNy0xNzsxMTo1NDo0NCBQTTs4OzI4ODU="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="coffeePrice" type="Integer" array="False" size=""/>
            <assign variable="coffeePrice" expression="25"/>
            <declare name="teaPrice" type="Integer" array="False" size=""/>
            <assign variable="teaPrice" expression="20"/>
            <declare name="coffeeQty" type="Integer" array="False" size=""/>
            <assign variable="coffeeQty" expression="10"/>
            <declare name="teaQty" type="Integer" array="False" size=""/>
            <assign variable="teaQty" expression="0"/>
            <declare name="menu" type="Integer" array="False" size=""/>
            <assign variable="menu" expression="1"/>
            <declare name="qty" type="Integer" array="False" size=""/>
            <declare name="total" type="Integer" array="False" size=""/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="menu"/>
            <if expression="menu=1">
                <then>
                    <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                    <input variable="qty"/>
                    <if expression="qty&lt;coffeeQty">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <assign variable="total" expression="coffeePrice*qty"/>
                            <output expression="&quot;Total Price : &quot;&amp;total&amp;&quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                    <input variable="qty"/>
                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>