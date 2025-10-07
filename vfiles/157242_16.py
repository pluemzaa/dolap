<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="TaoBin_VendingMachine_Corrected_For_Grader"/>
        <attribute name="authors" value="AI Assistant"/>
        <attribute name="about" value="Flowchart ฉบับแก้ไขสำหรับระบบตรวจโปรแกรมโดยเฉพาะ"/>
        <attribute name="saved" value="2024-07-19 10:30:00 AM"/>
        <attribute name="created" value="QVNVUztMQVBUT1AtTVVIVTVGSEc7MjU2OC0wNy0xOTsxMDowMDowMCBBTTsyNzAx"/>
        <attribute name="edited" value="QVNVUztMQVBUT1AtTVVIVTVGSEc7MjU2OC0wNy0xOTsxMDowMDowMCBBTTs5OzI4MDk="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="menu" type="Integer" array="False" size=""/>
            <declare name="quantity" type="Integer" array="False" size=""/>
            <declare name="totalPrice" type="Integer" array="False" size=""/>
            <declare name="coffeePrice" type="Integer" array="False" size=""/>
            <declare name="coffeeQty" type="Integer" array="False" size=""/>
            <declare name="teaPrice" type="Integer" array="False" size=""/>
            <declare name="teaQty" type="Integer" array="False" size=""/>
            <assign variable="coffeePrice" expression="25"/>
            <assign variable="coffeeQty" expression="10"/>
            <assign variable="teaPrice" expression="20"/>
            <assign variable="teaQty" expression="0"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - &quot; &amp; coffeePrice &amp; &quot; Baht - Qty: &quot; &amp; coffeeQty" newline="True"/>
            <output expression="&quot;2. Tea - &quot; &amp; teaPrice &amp; &quot; Baht - Qty: &quot; &amp; teaQty" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="menu"/>
            <if expression="menu == 1">
                <then>
                    <if expression="coffeeQty > 0">
                        <then>
                            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                            <input variable="quantity"/>
                            <if expression="quantity &gt; 0 AND quantity &lt;= coffeeQty">
                                <then>
                                    <assign variable="totalPrice" expression="quantity * coffeePrice"/>
                                    <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                                    <output expression="&quot;Total Price : &quot; &amp; totalPrice &amp; &quot; Baht&quot;" newline="True"/>
                                    <output expression="&quot;Enjoy!&quot;" newline="True"/>
                                </then>
                                <else>
                                    <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                                </else>
                            </if>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="menu == 2">
                        <then>
                            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                            <input variable="quantity"/>
                            <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Invalid menu selection.&quot;" newline="True"/>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>