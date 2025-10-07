<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4.4"/>
        <attribute name="authors" value="LENOVO"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 09:02:57 PM"/>
        <attribute name="created" value="TEVOT1ZPO0xBUFRPUC1BR01TQlYzVDsyNTY4LTA3LTIyOzA3OjU3OjM1IFBNOzI4NjI="/>
        <attribute name="edited" value="TEVOT1ZPO0xBUFRPUC1BR01TQlYzVDsyNTY4LTA3LTIyOzA5OjAyOjU3IFBNOzI7Mjk2Nw=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, newMoney" type="Real" array="False" size=""/>
            <declare name="years, year" type="Integer" array="False" size=""/>
            <output expression="&quot; Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot; Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot; Input years: &quot;" newline="True"/>
            <input variable="years"/>
            <for variable="year" start="1" end="years" direction="inc" step="1">
                <assign variable="money" expression="money * (1 + interest / 100)"/>
                <output expression="&quot;Year &quot; &amp; year &amp; &quot;: &quot; &amp; money" newline="True"/>
            </for>
        </body>
    </function>
</flowgorithm>