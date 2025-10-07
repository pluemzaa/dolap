<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="testflow4"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 08:26:57 PM"/>
        <attribute name="created" value="VXNlcjtERVNLVE9QLTZPS0QxVTI7MjU2OC0wNy0xNjswNTo0MjoxMSBQTTsyNzUw"/>
        <attribute name="edited" value="VXNlcjtERVNLVE9QLTZPS0QxVTI7MjU2OC0wNy0xNjswODoyNjo1NyBQTTs1OzI4Nzc="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest" type="Real" array="False" size=""/>
            <declare name="year, i" type="Integer" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <while expression="i &lt; year">
                <assign variable="money" expression="money*(1+interest/100)"/>
                <output expression="&quot;Year&quot; &amp; (i+1) &amp; &quot;:&quot; &amp; money" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>