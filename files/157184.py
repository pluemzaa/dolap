<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="work_flowforithm_4"/>
        <attribute name="authors" value="Vivobook"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 06:47:42 PM"/>
        <attribute name="created" value="Vml2b2Jvb2s7TEFQVE9QLTFEODVNVU02OzI1NjgtMDctMTY7MDY6MjQ6MjAgUE07MzE2OA=="/>
        <attribute name="edited" value="Vml2b2Jvb2s7TEFQVE9QLTFEODVNVU02OzI1NjgtMDctMTY7MDY6NDc6NDIgUE07MTszMjg1"/>
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
                <assign variable="money" expression="money * (1 + interest/100)"/>
                <output expression="&quot;Year&quot; &amp; (i+1) &amp; &quot;:&quot; &amp; money" newline="True"/>
                <assign variable="i" expression="i + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>